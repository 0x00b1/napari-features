import typing

import qtpy.QtWidgets
import qtpy.QtCore


class FeatureSelectionWidget(qtpy.QtWidgets.QWidget):
    def __init__(
        self,
        flags: typing.Union[qtpy.QtCore.Qt.WindowFlags, qtpy.QtCore.Qt.WindowType] = qtpy.QtCore.Qt.WindowFlags(),
    ):
        super(FeatureSelectionWidget, self).__init__(flags=flags)

