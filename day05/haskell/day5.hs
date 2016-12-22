import Data.List (isPrefixOf)
import Data.Hash.MD5

hashes :: String -> [String]
hashes = filter (isPrefixOf "00000") . zipWith (curry f) [1..] . repeat
    where f (a, b) = md5s . Str $ b ++ show a

part1 :: String -> String
part1 = map (!! 5) . take 8 . hashes

main :: IO ()
main = print . part1 $ "ugkcyxxp"