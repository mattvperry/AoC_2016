import Data.List (find)

expand :: String -> String
expand s = s ++ ['0'] ++ (reverse . map invert $ s)
    where invert c = if c == '0' then '1' else '0'

checksum :: String -> String
checksum [] = []
checksum (x:y:zs) = bit x y : checksum zs
    where bit a b = if a == b then '1' else '0'

fill :: Int -> String -> Maybe String
fill l x = f x >>= (g . take l)
    where f = find ((> l) . length) . iterate expand
          g = find (odd . length) . iterate checksum

main :: IO ()
main = do
    let input = "00101000101111010"
    print . fill 272 $ input
    print . fill 35651584 $ input