import Control.Arrow (first)
import Data.List (findIndex)

time :: [(Int, Int)] -> Maybe Int
time = findIndex (all $ uncurry isSlot) . go . zip [1..]
    where go i = [map (first (+x)) i | x <- [0..]]
          isSlot o (s, p) = (o + s) `mod` p == 0

main :: IO ()
main = do
    let discs = [(0, 7), (0, 13), (2, 3), (2, 5), (0, 17), (7, 19)]
    print . time $ discs
    print . time $ discs ++ [(0, 11)]