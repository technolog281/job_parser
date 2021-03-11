# from stov_script import max_page_counter, extract_hh_jobs
# #
# # max_page = max_page_counter()
# #
# # extract_hh_jobs(max_page)
# #
# # print(extract_hh_jobs(max_page))
# max_page = max_page_counter()
#
# x = extract_hh_jobs(max_page)
#
# print(x)

from SOF_lxml_script import max_page_counter, extract_hh_jobs, listmerge

max_page = max_page_counter()

result = extract_hh_jobs(max_page)

print(len(listmerge(result)))

