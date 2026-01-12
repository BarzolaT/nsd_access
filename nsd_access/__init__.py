"""
Automatically configures matplotlib backend
"""
import matplotlib
from ._gui_helpers import X_is_running, isnotebook

if not X_is_running() and not isnotebook():
    print('No X server detected. Changing matplotlib backend to Agg for compatibility.')
    matplotlib.use('Agg')
