from server.utilites import BusinessLogicFailure



def mok_business_service_with_error() -> None:
    '''
    Fake failed business scenario
    '''

    raise BusinessLogicFailure
