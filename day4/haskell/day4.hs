import Control.Arrow ((&&&))
import Data.List (break, group, sort)

type Room = (String, Integer, String)

getName :: Room -> String
getName (n, _, _) = n

getId :: Room -> Integer
getId (_, i, _) = i

getCsc :: Room -> String
getCsc (_, _, c) = c

readInput :: IO ([String])
readInput = lines <$> readFile "../input.txt"

parseRoom :: String -> Room
parseRoom = parse . breakOnLast '-'
    where breakOnLast c = break (==c) . reverse
          parse (a, b) = let (c, d) = breakOnLast '[' $ a in
              (init . reverse $ b, read c, init . tail $ d)

counter :: Ord a => [a] -> [(a, Int)]
counter = map (head &&& length) . group . sort

calculateCsc :: String -> String
calculateCsc = take 5 . map snd . sort . map go . counter . filter (/='-')
    where go (a, b) = (negate b, a)

validRoom :: Room -> Bool
validRoom = (==) <$> getCsc <*> calculateCsc . getName

part1 :: [Room] -> Integer
part1 = sum . map getId

main :: IO ()
main = do
    validRooms <- filter validRoom . map parseRoom <$> readInput
    print . part1 $ validRooms