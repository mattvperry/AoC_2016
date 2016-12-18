import Data.List (tails)

next :: String -> String
next xs = [rule x y | (x:_:y:_) <- tails ("." ++ xs ++ ".")]
    where rule x y
            | x == y    = '.'
            | otherwise = '^'

tiles :: Int -> String -> Int
tiles n = count . take n . iterate next
    where count = length . filter (=='.') . concat

main :: IO ()
main = do
    let input = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."
    print . tiles 40     $ input
    print . tiles 400000 $ input