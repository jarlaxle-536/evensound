from logic.functions import *

from logic.loader import *

class TrackRepresentationWidget(QWidget):
    _widgets = [
        'TrackCanvasLabel',
    ]

class TrackCanvasLabel(QLabel):
    _dependent_on = ['TrackSelector', 'Bar']
    def setup(self):
        super().setup()
        self.setAlignment(QtCore.Qt.AlignCenter)
    def update(self):
        print(f'{self}:update')
        pixmap = convert_pil_image_to_pixmap(self.create_image())
        pixmap = pixmap.scaled(800, 600, QtCore.Qt.KeepAspectRatio)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setPixmap(pixmap)
    def create_image(self):
        track = self._TrackSelector.object().selected
        bar = self._Composition.object().bars[0]
        width, height = 100, 25
        image = Image.new(mode='RGB', size=(width, height), color=(255, ) * 3)
        draw = ImageDraw.Draw(image)
        for note in bar.notes:
            print(note)
            print(bar.time_signature)
            middle = (note.start_position + note.ending_position) / 2
            image_pos = tuple(map(int, (middle / 16 * width, height / 2)))
            print(f'middle: {middle}')
            print(f'image_pos: {image_pos}')
            draw.text(image_pos, str(note.pitch), (0,) * 3)
        return image
