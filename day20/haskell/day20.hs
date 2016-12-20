import Control.Arrow ((***), (&&&))
import Data.List (sort, break)
import Data.Tuple (swap)

intervals :: [String] -> [(Int, Int)]
intervals = sort . map parse
    where parse = (read *** read . tail) . break (=='-')

merge :: [(Int, Int)] -> [(Int, Int)] -> [(Int, Int)]
merge xs []     = reverse xs
merge [] (y:ys) = merge [y] ys
merge (x@(xl, xh):xs) (y@(yl, yh):ys)
    | xh <= yl  = merge (y:x:xs) ys
    | xh <  yh  = merge ((xl, yh):xs) ys
    | otherwise = merge (x:xs) ys

solve :: [String] -> (Int, Int)
solve = (lowest &&& total) . merge [] . intervals
    where lowest = (+1) . snd . head
          total = sum . map f . (zip <*> tail)
          f = subtract 1 . uncurry (-) . swap . (snd *** fst)

main :: IO ()
main = do
    input <- lines <$> readFile "../input.txt"
    print . solve $ input