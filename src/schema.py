from pydantic import BaseModel, validator


responses_list = ['ERROR', 'SUCCESS', 'VERSION']


class RequestResponse(BaseModel):
    response_text: str

    @validator('response_text')
    def apply_error_message(cls, v):
        message = v.split(':')[0]
        if message == 'ERROR':
            raise ValueError(v)
        return v
