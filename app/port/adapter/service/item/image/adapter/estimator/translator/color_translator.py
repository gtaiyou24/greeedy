from domain.model.color import Color


class ColorTranslator:
    def from_(self, response: dict) -> list[Color]:
        return [Color.value_of(prediction['color']) for prediction in response['colors']]
