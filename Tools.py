from log import module_log

logger = module_log('tools.log')

# guard of any none input will throw in the pass argument
def is_none(*args) -> bool:
    logger.log.info(f'argument:{args}')
    #log.debug(f'{args}')
    for data in args:                # check if any in the argument that being pass are None
        if data == None:
            return True
    return False


