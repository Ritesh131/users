import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.RtcTokenBuilder import *


def main():
    appID = "64d0d0ef1715448dae4298949d2bf4a2"
    appCertificate = "82e3c49f17154c1b86df44d77135b073"
    channelName = "7d72365eb983485397e3e3f9d460bdda"
    uid = 0
    userAccount = "2882341273"
    expireTimeInSeconds = 3600
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expireTimeInSeconds

    token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, Role_Attendee, privilegeExpiredTs)
    print("Token with int uid: {}".format(token))
    
    # token = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)
    # print("Token with user account: {}".format(token))

    # token = RtcTokenBuilder.buildTokenWithUidAndPrivilege(appID, appCertificate, channelName, uid, 
    #                                           privilegeExpiredTs, privilegeExpiredTs,
    #                                           privilegeExpiredTs, privilegeExpiredTs)
    # print("Token with int uid user defined privilege: {}".format(token))

    # token = RtcTokenBuilder.buildTokenWithUserAccountAndPrivilege(appID, appCertificate, channelName, userAccount,
    #                                               privilegeExpiredTs, privilegeExpiredTs,
    #                                               privilegeExpiredTs, privilegeExpiredTs)
    # print("Token with user account user defined privilege: {}".format(token))

if __name__ == "__main__":
    main()