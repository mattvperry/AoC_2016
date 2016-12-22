import Data.List (elemIndex, splitAt)

data Instruction = 
    Swap Char Char 
    | SwapPos Int Int 
    | Move Int Int 
    | Reverse Int Int 
    | RotatePos Char 
    | RotateLeft Int 
    | RotateRight Int
    deriving (Show)

parse :: [String] -> Instruction
parse ["swap", "position", x, _, _, y]  = SwapPos       (read x) (read y)
parse ["swap", "letter", x, _, _, y]    = Swap          (head x) (head y)
parse ["rotate", "left", x, _]          = RotateLeft    (read x)
parse ["rotate", "right", x, _]         = RotateRight   (read x)
parse ["rotate", _, _, _, _, _, x]      = RotatePos     (head x)
parse ["reverse", _, x, _, y]           = Reverse       (read x) (read y)
parse ["move", _, x, _, _, y]           = Move          (read x) (read y)

exec :: String -> Instruction -> String
exec s (Swap a b)       = map swap s
    where swap c
            | c == a    = b
            | c == b    = a
            | otherwise = c
exec s (SwapPos x y)    = map (snd . swap) . zip [0..] $ s
    where swap t@(i, _)
            | i == x    = (i, s !! y)
            | i == y    = (i, s !! x)
            | otherwise = t
exec s (RotateLeft x)   = drop n s ++ take n s
    where n = x `mod` length s
exec s (RotateRight x)  = exec s (RotateLeft n)
    where n = length s - x
exec s (RotatePos c)    = exec s (RotateRight (f . elemIndex c $ s))
    where f (Just x)
            | x >= 4    = x + 2
            | otherwise = x + 1
exec s (Reverse x y)    = take x s ++ m ++ drop (y + 1) s
    where m = reverse . take (y - x + 1) . drop x $ s
exec s (Move x y)       = c ++ b:d
    where (a, b:bs)   = splitAt x s
          (c, d)        = splitAt y (a ++ bs)

execR :: String -> Instruction -> String
execR s (Swap a b)       = exec s (Swap a b)
execR s (SwapPos x y)    = exec s (SwapPos x y)
execR s (RotateLeft x)   = exec s (RotateRight x)
execR s (RotateRight x)  = exec s (RotateLeft x)
execR s (Reverse x y)    = exec s (Reverse x y)
execR s (Move x y)       = exec s (Move y x)
execR s (RotatePos c)    = head $ filter f [exec s (RotateLeft x) | x <- [1..]]
    where f = (== s) . flip exec (RotatePos c)

run :: (String -> Instruction -> String) -> String -> [String] -> String
run f s = foldl f s . map (parse . words)

main :: IO ()
main = do
    input <- lines <$> readFile "../input.txt"
    print $ run exec  "abcdefgh" input
    print $ run execR "fbgdceah" (reverse input)