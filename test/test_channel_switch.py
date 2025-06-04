from custom_components.artnet_led.util.channel_switch import to_values, from_values

mid_k = 4268
min_k = 2000
max_k = 6536

def test_to_values_ch():
    values = to_values("ch", 1, True, 255, cold_white=255, warm_white=128)

    assert values[0] == 255
    assert values[1] == 128

    values = to_values("ch", 1, True, 255, cold_white=128, warm_white=64)

    assert values[0] == 255
    assert values[1] == 127

    values = to_values("ch", 1, True, 128, cold_white=128, warm_white=64)
    assert values[0] == 128
    assert values[1] == 64


def test_to_values_dCH():
    values = to_values("dCH", 1, True, 255, cold_white=255, warm_white=128)

    assert values[0] == 255
    assert values[1] == 255
    assert values[2] == 128

    values = to_values("dCH", 1, True, 255, cold_white=128, warm_white=64)

    assert values[0] == 255
    assert values[1] == 255
    assert values[2] == 127

    values = to_values("dCH", 1, True, 128, cold_white=128, warm_white=64)
    assert values[0] == 128
    assert values[1] == 255
    assert values[2] == 127


def test_to_values_color_temp():
    values = to_values("ch", 1, True, 255,
                       color_temp_kelvin=mid_k, 
                       min_kelvin=min_k, 
                       max_kelvin=max_k)

    assert values[0] >= 254
    assert values[1] >= 254


def test_from_values_ch():
    is_on, brightness, _, _, _, cold_white, warm_white, color_temp = \
        from_values("ch", 1, [255, 0], 
                    min_kelvin=min_k, 
                    max_kelvin=max_k)

    assert is_on
    assert brightness == 255
    assert cold_white == 255
    assert warm_white == 0
    assert color_temp == max_k

    is_on, brightness, _, _, _, cold_white, warm_white, color_temp = \
        from_values("ch", 1, [0, 255], 
                       min_kelvin=min_k, 
                       max_kelvin=max_k)

    assert is_on
    assert brightness == 255
    assert cold_white == 0
    assert warm_white == 255
    assert color_temp == min_k

    is_on, brightness, _, _, _, cold_white, warm_white, color_temp = \
        from_values("ch", 1, [255, 255], 
                       min_kelvin=min_k, 
                       max_kelvin=max_k)

    assert is_on
    assert brightness == 255
    assert cold_white == 255
    assert warm_white == 255
    assert color_temp == mid_k

    is_on, brightness, _, _, _, cold_white, warm_white, color_temp = \
        from_values("ch", 1, [128, 128],  
                       min_kelvin=min_k, 
                       max_kelvin=max_k)

    assert is_on
    assert brightness == 128
    assert cold_white == 255
    assert warm_white == 255
    assert color_temp == mid_k

def test_from_values_dCH():
    is_on, brightness, _, _, _, cold_white, warm_white, color_temp = \
        from_values("dCH", 1, [255, 255, 0],  
                       min_kelvin=min_k, 
                       max_kelvin=max_k)

    assert is_on
    assert brightness == 255
    assert cold_white == 255
    assert warm_white == 0
    assert color_temp == max_k

    is_on, brightness, _, _, _, cold_white, warm_white, color_temp = \
        from_values("dCH", 1, [255, 0, 255],  
                       min_kelvin=min_k, 
                       max_kelvin=max_k)

    assert is_on
    assert brightness == 255
    assert cold_white == 0
    assert warm_white == 255
    assert color_temp == min_k

    is_on, brightness, _, _, _, cold_white, warm_white, color_temp = \
        from_values("dCH", 1, [255, 255, 255],  
                       min_kelvin=min_k, 
                       max_kelvin=max_k)

    assert is_on
    assert brightness == 255
    assert cold_white == 255
    assert warm_white == 255
    assert color_temp == mid_k

    is_on, brightness, _, _, _, cold_white, warm_white, color_temp = \
        from_values("dCH", 1, [255, 128, 128],  
                       min_kelvin=min_k, 
                       max_kelvin=max_k)

    assert is_on
    assert brightness == 255
    assert cold_white == 128
    assert warm_white == 128
    assert color_temp == mid_k

    is_on, brightness, _, _, _, cold_white, warm_white, color_temp = \
        from_values("dCH", 1, [128, 255, 255],  
                       min_kelvin=min_k, 
                       max_kelvin=max_k)

    assert is_on
    assert brightness == 128
    assert cold_white == 255
    assert warm_white == 255
    assert color_temp == mid_k
