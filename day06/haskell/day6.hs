import Control.Arrow ((&&&))
import Data.List (transpose, sort, group)

colFreq :: Ord a => [a] -> [a]
colFreq = map snd . sort . count
    where count = map (length &&& head) . group . sort

decode :: Ord a => ([a] -> a) -> [[a]] -> [a]
decode f = map (f . colFreq) . transpose

main :: IO ()
main = do
    input <- lines <$> readFile "../input.txt"
    print (decode last input, decode head input)