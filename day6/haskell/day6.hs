import Control.Arrow ((&&&))
import Data.List (transpose, sort, sortBy, group)
import Data.Ord (comparing)

colFreq :: Ord a => [a] -> [a]
colFreq = map fst . sortBy (comparing snd) . freqs
    where freqs = map (head &&& length) . group . sort

decode :: Ord a => ([a] -> a) -> [[a]] -> [a]
decode f = map (f . colFreq) . transpose

main :: IO ()
main = do
    input <- lines <$> readFile "../input.txt"
    print . decode last $ input
    print . decode head $ input