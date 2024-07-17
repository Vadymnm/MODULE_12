import requests as rq
import logging


log_info = logging.getLogger('info')
log_info.setLevel(logging.INFO)
fh = logging.FileHandler("success_responce.log", 'w', 'utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
log_info.addHandler(fh)

log_error = logging.getLogger('error')
log_error.setLevel(logging.ERROR)
fh1 = logging.FileHandler("blocked_responses.log", 'w', 'utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh1.setFormatter(formatter)
log_error.addHandler(fh1)

log_warn = logging.getLogger('warning')
log_warn.setLevel(logging.WARNING)
fh2 = logging.FileHandler("bad_responses.log", 'w', 'utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh2.setFormatter(formatter)
log_warn.addHandler(fh2)


sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']


def my_log(site):
    for site in sites:
        try:
            response = rq.get(site, timeout=3)
            message = (site, 'response - ', response.status_code)
            print(message)
            if response.status_code == 200:
                log_info.info(message)
            else:
            #if response.status_code != 200:  #403 or response.status_code == 503 :
                message = (site, 'WARNING', response.status_code)
                log_warn.warning(message)
        except:
            message = (site, 'NO  CONNECTION')
            log_error.error(message, exc_info=False)

my_log(sites)

