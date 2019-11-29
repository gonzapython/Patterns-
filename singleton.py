class SoyUnico(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = object.__new__(cls)
        return cls.instance



# ----------

lorenzo = SoyUnico()
print(f' Lorenzo es:  {lorenzo}')

leonor = SoyUnico()
print(f' Leonor es:   {leonor}')

mario = SoyUnico()
print(f' Mario es:    {mario}')

veronica = SoyUnico()
print(f' Verónica es: {veronica}')


