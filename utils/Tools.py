from logs.log import module_log

logger = module_log(log_name = 'tools.log',disable_log = False)

# guard of any none input will throw in the pass argument
def is_none(*args) -> bool:
    logger.log.debug(f'input:{args}')
    for data in args:                # check if any in the argument that being pass are None
        logger.log.debug(f'input:{data}')
        if data == None:
            logger.log.debug(f'argument:{args} - evaluation: {True}')
            return True
    logger.log.debug(f'argument:{args} - evaluation: {False}')
    return False
