# -*- coding:utf-8 -*-

import os
from dotenv import load_dotenv
from mailchimp3 import MailChimp

load_dotenv()

# client = MailChimp(mc_api=os.getenv('MC_API_KEY'), mc_user=os.getenv('MC_USER_NAME'))

# aa = client.lists.all(get_all=True, fields="lists.name,lists.id")
# aa = client.lists.members.all('58c9187424', True, fields="members.email_address,members.id")
aa = 'https://us4.api.mailchimp.com/3.0/lists/58c9187424/members' # YA da buraya curl&requests ile get gönderebilirsin !
print(aa)
