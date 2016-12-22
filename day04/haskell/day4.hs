import Control.Arrow ((&&&))
import Data.List (cycle, break, find, group, isPrefixOf, sort)
import Data.Maybe (fromJust)

type Room = (String, Int, String)

getName :: Room -> String
getName (n, _, _) = n

getId :: Room -> Int
getId (_, i, _) = i

getCsc :: Room -> String
getCsc (_, _, c) = c

readInput :: IO [String]
readInput = lines <$> readFile "../input.txt"

parseRoom :: String -> Room
parseRoom = parse . breakOnLast '-'
    where breakOnLast c = break (==c) . reverse
          parse (a, b) = let (c, d) = breakOnLast '[' a in
              (init . reverse $ b, read c, init . tail $ d)

counter :: Ord a => [a] -> [(a, Int)]
counter = map (head &&& length) . group . sort

calculateCsc :: String -> String
calculateCsc = take 5 . map snd . sort . map f . counter . filter (/='-')
    where f (a, b) = (negate b, a)

validRoom :: Room -> Bool
validRoom = (==) <$> getCsc <*> calculateCsc . getName

decryptChar :: Int -> Char -> Char
decryptChar _ '-'   = ' '
decryptChar n c     = ([c .. 'z'] ++ cycle ['a' .. 'z']) !! n

decryptName :: Room -> Room
decryptName (n, i, c) = (map (decryptChar i) n, i, c)

part1 :: [Room] -> Int
part1 = sum . map getId

part2 :: [Room] -> Int
part2 = getId . fromJust . find (isPrefixOf "northpole" . getName) . map decryptName

main :: IO ()
main = do
    validRooms <- filter validRoom . map parseRoom <$> readInput
    print . part1 $ validRooms
    print . part2 $ validRooms