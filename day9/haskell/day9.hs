import Control.Arrow ((***))
import Data.List (break)

marker :: String -> (Maybe (Int, Int), String)
marker ('(':xs) = (Just . parse *** tail) . break (==')') $ xs
    where parse = (read *** read . tail) . break (=='x')
marker s = (Nothing, s)

decompress :: Bool -> String -> Int
decompress b = go b . marker
    where go _ (_, []) = 0
          go _ (Nothing, s) = 1 + rec tail s
          go False (Just (l, t), s) = l * t + rec (drop l) s
          go True (Just (l, t), s) = rec (take l) s * t + rec (drop l) s
          rec f = decompress b . f

main :: IO ()
main = do
    input <- readFile "../input.txt"
    print . decompress False $ input
    print . decompress True $ input