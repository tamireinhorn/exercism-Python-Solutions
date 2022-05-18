from collections import namedtuple


Bucket = namedtuple('bucket', 'name capacity current')

def measure(bucket_one, bucket_two, goal, start_bucket):
    if goal > bucket_one and goal > bucket_two:
        raise ValueError("Goal can't be bigger than both buckets.")
    def empty_bucket(buckets, bucket_to_empty):
        nonlocal actions 
        actions += 1
        b = buckets[bucket_to_empty]
        if b.current == 0:
            return False 
        buckets[bucket_to_empty] = Bucket(b.name, b.capacity, 0)
        return buckets

    def fill_bucket(buckets, bucket_to_fill):
        nonlocal actions
        actions += 1
        b = buckets[bucket_to_fill]
        if b.current == b.capacity:
            return False 
        buckets[bucket_to_fill] = Bucket(b.name, b.capacity, b.capacity)
        return buckets

    def transfer(bucket_list, bucket_from_index, bucket_to_index):
        nonlocal actions
        actions += 1
        bucket_to = bucket_list[bucket_to_index]
        bucket_from = bucket_list[bucket_from_index]
        avaliable_space = bucket_to.capacity - bucket_to.current
        if avaliable_space == 0 or bucket_from.current == 0:
            return False 
        # If there's more space than volume to be transferred: 
        if avaliable_space >= bucket_from.current:
            bucket_to = Bucket(bucket_to.name, bucket_to.capacity, bucket_to.current + bucket_from.current)
            bucket_from = Bucket(bucket_from.name, bucket_from.capacity, 0)
        else:
            bucket_to = Bucket(bucket_to.name, bucket_to.capacity, bucket_to.capacity)
            bucket_from = Bucket(bucket_from.name, bucket_from.capacity, bucket_from.current - avaliable_space)
        bucket_list[bucket_to_index] = bucket_to 
        bucket_list[bucket_from_index] = bucket_from
        return bucket_list

    def parse_bucket_number(string):
        diction = {'one': 0, 'two': 1}
        reverse_diction = {0: 'one', 1: 'two'}
        if string in diction:
            return diction.get(string)
        if string in reverse_diction:
            return reverse_diction.get(string)

    def is_over(buckets):
        nonlocal goal 
        for bucket in buckets:
            if bucket.current == goal:
                return True
        return False 

    def is_empty(bucket):
        return bucket.current == 0
    
    def is_full(bucket):
        return bucket.capacity == bucket.current
    
    def is_partially_filled(bucket):
        return not is_full(bucket) and not is_empty(bucket)
    actions = 0
    start_bucket = parse_bucket_number(start_bucket)
    other_bucket = 0 if start_bucket else 1
    #Initialize bucket list
    buckets = [Bucket('bucket_1', bucket_one, 0), Bucket('bucket_2', bucket_two, 0)]
    while not is_over(buckets):
        # I solved this exercise by effectively walking through some of the tests and seeing what actions I could take and the pattern.
        first_bucket = buckets[start_bucket]
        second_bucket = buckets[other_bucket]
        # We always fill the start bucket if it is empty and the other is also empty
        if is_empty(first_bucket) and is_empty(second_bucket):
            buckets = fill_bucket(buckets, start_bucket)
        # If we can solve it by filling the second bucket right away, just fill it.
        elif goal == second_bucket.capacity and not is_empty(first_bucket):
            buckets = fill_bucket(buckets, other_bucket)
        # If the start bucket is full, all we can do is transfer from it.
        # We can't transfer if the second is full, but that will ONLY happen if it's a win condition. 
        elif is_full(first_bucket):
            # Then, we transfer from the filled bucket:
            buckets = transfer(buckets, start_bucket, other_bucket)
        # If the first bucket is empty and the second has something, the only possible action is to fill the first bucket.
        # Why not transfer? Because partials only appear DUE to transfer. So if the second bucket is partial, transfer already happened, thus it's pointless.
        elif is_empty(first_bucket) and is_partially_filled(second_bucket):
            buckets = fill_bucket(buckets, start_bucket)
        # If the first bucket is partially, and the second is full, we can only empty the second. Empty first is a rule break.
        # Why not transfer from the second to the first?  Again, because partials only exist post transfer.
        # So if the first is partial, it's because we already did a transfer from 1 to 2. So no point in doing it backwards.
        elif is_partially_filled(first_bucket) and is_full(second_bucket):
            buckets = empty_bucket(buckets, other_bucket)
        # If we have an empty bucket in 2, AND the first one isn't filled, it's because we did the above elif.
        # So filling the second bucket would be a loop, filling the first one is going back to the start (we always fill the first one)
        # Ergo, all we can do is a transfer!
        elif is_partially_filled(first_bucket) and is_empty(second_bucket):
            buckets = transfer(buckets, start_bucket, other_bucket)
        elif is_empty(first_bucket) and is_full(second_bucket):
            # Should this happen, this is a rule break and means the scenario is impossible. 
            raise ValueError("This combination is impossible without breaking the rules.")
    bucket_with_goal = [i for i, j in enumerate(buckets) if j.current == goal][0]
    bucket_without_goal = 0 if bucket_with_goal == 1 else 1 
    return actions, parse_bucket_number(bucket_with_goal), buckets[bucket_without_goal].current