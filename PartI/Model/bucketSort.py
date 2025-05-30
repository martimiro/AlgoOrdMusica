'''
BUCKET SORT
COMPLEXITAT: O(n²)
'''

class BucketSort:
    def bucket_sort(self, llista):
        if len(llista) == 0:
            return

        n = len(llista)
        min_val = min(llista)
        max_val = max(llista)
        range_val = max_val - min_val + 1  # +1 per incloure el màxim

        num_buckets = n
        buckets = [[] for _ in range(num_buckets)]

        for num in llista:
            bi = (num - min_val) * num_buckets // range_val
            if bi >= num_buckets:
                bi = num_buckets - 1
            buckets[bi].append(num)

        iteracio = 1
        index = 0
        for bucket in buckets:
            for i in range(1, len(bucket)):
                key = bucket[i]
                j = i - 1
                while j >= 0 and bucket[j] > key:
                    bucket[j + 1] = bucket[j]
                    j -= 1
                bucket[j + 1] = key

            for num in bucket:
                llista[index] = num
                index += 1

            print(f"Iteració: {iteracio}")
            print(llista)
            iteracio += 1