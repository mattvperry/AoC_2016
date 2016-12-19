using System;
using System.Collections.Generic;
using System.Linq;

namespace Day19
{
    public static class Program
    {
        public static LinkedListNode<T> NextOrFirst<T>(this LinkedListNode<T> current)
        {
            return current.Next ?? current.List.First;
        }

        public static int Part1(int size)
        {
            var ll = new LinkedList<int>(Enumerable.Range(1, size));
            var curr = ll.First;
            while(ll.Count > 1)
            {
                ll.Remove(curr.NextOrFirst());
                curr = curr.NextOrFirst();
            }

            return ll.First.Value;
        }

        public static int Part2(int size)
        {
            var ll = new LinkedList<int>(Enumerable.Range(1, size));
            var curr = ll.First;
            var acc = curr;
            foreach (var _ in Enumerable.Range(0, ll.Count / 2))
            {
                acc = acc.NextOrFirst();
            }

            while(ll.Count > 1)
            {
                var temp = acc;
                acc = acc.NextOrFirst();
                if (ll.Count % 2 != 0)
                {
                    acc = acc.NextOrFirst();
                }
                ll.Remove(temp);
                curr = curr.NextOrFirst();
            }

            return ll.First.Value;
        }

        public static void Main(string[] args)
        {
            Console.WriteLine(Part1(3014603));
            Console.WriteLine(Part2(3014603));
        }
    }
}