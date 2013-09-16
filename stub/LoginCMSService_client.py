##################################################
# file: LoginCMSService_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     /usr/bin/wsdl2py LoginCms?WSDL
# 
##################################################

from LoginCMSService_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI

# Locator
class LoginCMSServiceLocator:
    LoginCms_address = "https://wsaahomo.afip.gov.ar/ws/services/LoginCms"
    def getLoginCmsAddress(self):
        return LoginCMSServiceLocator.LoginCms_address
    def getLoginCms(self, url=None, **kw):
        return LoginCmsSoapBindingSOAP(url or LoginCMSServiceLocator.LoginCms_address, **kw)

# Methods
class LoginCmsSoapBindingSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: loginCms
    def loginCms(self, request, **kw):
        if isinstance(request, loginCmsRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(loginCmsResponse.typecode)
        return response

loginCmsRequest = GED("http://wsaa.view.sua.dvadac.desein.afip.gov", "loginCms").pyclass

loginCmsResponse = GED("http://wsaa.view.sua.dvadac.desein.afip.gov", "loginCmsResponse").pyclass
