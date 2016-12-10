import Control.Arrow (first, (***), (&&&))
import Control.Monad (liftM2)
import Data.List (tails, isInfixOf)
import Data.Tuple (swap)

windows :: Int -> [a] -> [[a]]
windows n = takeWhile ((== n) . length) . map (take n) . tails

splitWith :: (a -> Bool) -> [a] -> [[a]]
splitWith f = go . break f
    where go ([], _) = [[]]
          go (a, []) = [a] 
          go (a, b)  = a : (go . break f . tail $ b) 

isBracket :: Char -> Bool
isBracket = (||) <$> (== '[') <*> (== ']')

isAbba :: Eq a => [a] -> Bool
isAbba [a,b,c,d] = and [a == d, b == c, a /= b]
isAbba _ = False

hasAbba :: Eq a => [a] -> Bool
hasAbba = any isAbba . windows 4

isAba :: Eq a => [a] -> Bool
isAba [a, b, c] = and [a == c, a /= b]
isAba _ = False

findBabs :: String -> [String]
findBabs = map toBab . filter isAba . windows 3
    where toBab [a,b,_] = [b,a,b]

splitIp :: String -> ([String], [String])
splitIp = foldr f ([], []) . splitWith isBracket
    where f x = first (x:) . swap

supportsTls :: String -> Bool
supportsTls = uncurry (&&) . (f *** not . f) . splitIp
    where f = any hasAbba

supportsSsl :: String -> Bool
supportsSsl = any f . uncurry (liftM2 (,)) . first (concatMap findBabs) . splitIp
    where f = uncurry isInfixOf

count :: (a -> Bool) -> [a] -> Int
count f = length . filter f

main :: IO ()
main = do
    input <- lines <$> readFile "../input.txt"
    print . (count supportsTls &&& count supportsSsl) $ input