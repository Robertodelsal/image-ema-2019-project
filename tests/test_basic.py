
""" Code unit-tests go here. """
import numpy as np

import image_ema_project

def test_roi_xy():
    """Test the roi_xy function"""
    xy = np.arange(-4, 5)   
    result = [xy, xy]
    roi_xy = image_ema_project.roi_xy([0, 0], [8, 8]) #[0,0] è il punto [8,8] indica la roi che voglio
    np.equal(roi_xy, result)
    np.all(np.equal(roi_xy,result)) #cioè sto confrontando cio che mi da roi con result e se è giusto il test è ok. np.all considera tutti i punti uno a uno e se è vera la condizione np.equal per ogni punto cioè sono uguali allora a posto
    assert np.all(np.equal(roi_xy,[xy,xy]))

#def test_roi_xy()
#"""Test the roi_xy function"""
#    xy = np.arange(-4, 5)
#    roi_xy = image_ema_project.roi_xy([0, 0], [8, 8])
#    assert np.all(np.equal(roy_xy,[xy,xy]))