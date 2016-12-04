import Data.List (transpose)

readInput :: IO ([String])
readInput = lines <$> readFile "../input.txt"

chunk :: Int -> [a] -> [[a]]
chunk _ []  = []
chunk n l   = take n l : (chunk n $ drop n l)

parseSides :: [String] -> [[Integer]]
parseSides = map (map read . words)

valid :: [Integer] -> Bool
valid (x:y:z:[])
    | x + y > z && y + z > x && x + z > y = True
    | otherwise = False
valid _ = False

rotate :: [[Integer]] -> [[Integer]]
rotate = concatMap (chunk 3) . transpose

countValid :: [[Integer]] -> Int
countValid = length . filter valid

main :: IO()
main = do
    input <- parseSides <$> readInput
    print . countValid $ input
    print . countValid . rotate $ input