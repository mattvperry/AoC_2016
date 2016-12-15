import Data.List (tails, findIndex)

discs :: [(Int, Int)]
discs = [(0, 7), (0, 13), (2, 3), (2, 5), (0, 17), (7, 19)]

windows :: Int -> [a] -> [[a]]
windows n = takeWhile ((== n) . length) . map (take n) . tails

isSlot :: (Int, Int) -> Int -> Bool
isSlot (o, p) t = (o + t) `mod` p == 0

time :: [(Int, Int)] -> Maybe Int
time ds = findIndex (all id) $ zipWith isSlot <$> repeat ds <*> runs ds
    where runs = drop 1 . flip windows [0..] . length

main :: IO ()
main = do
    print . time $ discs
    print . time $ discs ++ [(0, 11)]