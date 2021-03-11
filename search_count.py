from SOF_lxml_script import max_page_counter, extract_hh_jobs, listmerge


def search_count(params) -> int:
    max_page = max_page_counter(params)
    list_of_jobs = extract_hh_jobs(max_page)
    count = len(listmerge(list_of_jobs))
    return count
