# def lost_fragments(sent, received):
#     sent_words = sent.split()
#     received_words = received.split()

#     temp = received_words.copy()
#     lost = []

#     for word in sent_words:
#         if word in temp:
#             temp.remove(word)  # consume the word if available
#         else:
#             lost.append(word)  # otherwise, it's lost

#     return lost

# print(lost_fragments("I choose a lazy person to do a hard job", "choose a hard person"))




# def find_timed_out_services(timestamp, serviceId, threshold):
#     from collections import defaultdict

#     # Group timestamps by service ID
#     services = defaultdict(list)
#     for t, s in zip(timestamp, serviceId):
#         services[s].append(t)

#     timed_out = []

#     # Check each service
#     for svc, times in services.items():
#         times.sort()
#         for i in range(1, len(times)):
#             if times[i] - times[i - 1] > threshold:
#                 timed_out.append(svc)
#                 break  # stop checking this service

#     return sorted(timed_out)


# # Example 1
# timestamp = [10, 20, 80, 10, 65]
# serviceId = ["svc1", "svc1", "svc1", "svc2", "svc2"]
# threshold = 30

# print(find_timed_out_services(timestamp, serviceId, threshold))
# # Output: ['svc1', 'svc2']



# class userMainCode(object):
#     @classmethod
#     def getMaxAdjacentChars(cls, input1):
#         words = input1.strip().split()
#         ll = [word[-1] for word in words[:-1]]
#         fl = [word[0] for word in words[1:]]
        
#         from collections import Counter
        
#         lc = Counter(ll)
#         fc = Counter(fl)
        
#         ml = max(lc.values())
#         mf = max(fc.values())
        
#         cl = min([c for c, count in lc.items() if count == ml])
#         cf = min([c for c, count in fc.items() if count == mf])
        
#         print(f"{cl} {cf}")
#         return f"{cl} {cf}"
    


# from collections import Counter

# class userMainCode(object):
#     @classmethod
#     def schoolFundraiser(cls, input1, input2):
#         li = Counter(input1)
#         unique_only = [c for c, count in li.items() if count == 1]
#         return sum(unique_only)



# class userMainCode(object):
#     @classmethod
#     def addDigits(cls, input1):
#         '''
#         input : int

#         Excepted return type : int
#         '''

#         while input1>=10:
#             input1 = sum(int(d) for d in str(input1))
        
#         return input1


