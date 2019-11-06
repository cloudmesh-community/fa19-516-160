from cloudmesh.configuration.Config import Config
config = Config()
profile = config["cloudmesh.profile"]
print(profile)

##
"""
    flow = flow_from_clientsecrets(filename, scope, message=message,          #Change this to use jason as oblect
                                   cache=cache, redirect_uri=redirect_uri,
                                   device_uri=device_uri)
    credentials = flow.step2_exchange(code, http=http)
    return credentials
"""