"""Matplotlib based plotting."""
from discretisedfield.plotting.hv import Hv
from discretisedfield.plotting.k3d_field import K3dField
from discretisedfield.plotting.k3d_region import K3dRegion
from discretisedfield.plotting.mpl import add_colorwheel
from discretisedfield.plotting.mpl_field import MplField
from discretisedfield.plotting.mpl_region import MplRegion

from . import util

"""Default settings for plotting."""
defaults = util.Defaults()
