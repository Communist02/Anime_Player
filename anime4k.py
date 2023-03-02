import os

presets = {
    'Mode A (Fast)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_M.glsl',
        'Anime4K_Upscale_CNN_x2_M.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_S.glsl'
    ],
    'Mode A (HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_VL.glsl',
        'Anime4K_Upscale_CNN_x2_VL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_M.glsl'
    ],
    'Mode B (HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_Soft_VL.glsl',
        'Anime4K_Upscale_CNN_x2_VL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_M.glsl'
    ],
    'Mode C (HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Upscale_Denoise_CNN_x2_VL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_M.glsl'
    ],
    'Mode A+A (HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_VL.glsl', 'Anime4K_Upscale_CNN_x2_VL.glsl',
        'Anime4K_Restore_CNN_M.glsl', 'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl',
        'Anime4K_Upscale_CNN_x2_M.glsl'
    ],
    'Mode B+B (HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_Soft_VL.glsl', 'Anime4K_Upscale_CNN_x2_VL.glsl',
        'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Restore_CNN_Soft_M.glsl',
        'Anime4K_Upscale_CNN_x2_M.glsl'
    ],
    'Mode C+A (HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Upscale_Denoise_CNN_x2_VL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Restore_CNN_M.glsl', 'Anime4K_Upscale_CNN_x2_M.glsl'
    ],
    'Mode A (Ultra HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_GAN_UUL.glsl',
        'Anime4K_Upscale_GAN_x4_UL.glsl', 'Anime4K_Restore_CNN_Soft_UL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl'
    ],
    'Mode B (Ultra HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_Soft_UL.glsl',
        'Anime4K_Upscale_CNN_x2_UL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl'
    ],
    'Mode C (Ultra HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Upscale_Denoise_CNN_x2_UL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl'
    ],
    'Mode A+A (Ultra HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_GAN_UUL.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl',
        'Anime4K_Restore_GAN_UUL.glsl', 'Anime4K_Restore_CNN_Soft_UL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl'
    ],
    'Mode B+B (Ultra HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_Soft_UL.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl',
        'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Restore_CNN_Soft_UL.glsl',
        'Anime4K_Upscale_CNN_x2_UL.glsl'
    ],
    'Mode C+A (Ultra HQ)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Upscale_Denoise_CNN_x2_UL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Restore_GAN_UUL.glsl', 'Anime4K_Restore_CNN_Soft_UL.glsl',
        'Anime4K_Upscale_CNN_x2_UL.glsl'
    ],
    'Mode C+A (Died your PC)': [
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Upscale_Denoise_CNN_x2_UL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Restore_GAN_UUL.glsl', 'Anime4K_Upscale_GAN_x4_UL.glsl',
        'Anime4K_Restore_CNN_Soft_UL.glsl'
    ]
}

qualities = ['S', 'M', 'L', 'VL', 'UL']

modes = ['A', 'B', 'C', 'A+A', 'B+B', 'C+A']

sec_qualities = {'S': 'S', 'M': 'S', 'L': 'M', 'VL': 'M', 'UL': 'L'}

current_preset = presets['Mode A (HQ)']


def create_preset(quality, mode):
    created_presets = {
        'A': [
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Restore_CNN_{quality}.glsl',
            f'Anime4K_Upscale_CNN_x2_{quality}.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
            'Anime4K_AutoDownscalePre_x4.glsl', f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        ],
        'B': [
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Restore_CNN_Soft_{quality}.glsl',
            f'Anime4K_Upscale_CNN_x2_{quality}.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
            'Anime4K_AutoDownscalePre_x4.glsl', f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        ],
        'C': [
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Upscale_Denoise_CNN_x2_{quality}.glsl',
            'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl',
            f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        ],
        'A+A': [
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Restore_CNN_{quality}.glsl',
            f'Anime4K_Upscale_CNN_x2_{quality}.glsl', f'Anime4K_Restore_CNN_{sec_qualities[quality]}.glsl',
            'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl',
            f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        ],
        'B+B': [
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Restore_CNN_Soft_{quality}.glsl',
            f'Anime4K_Upscale_CNN_x2_{quality}.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
            'Anime4K_AutoDownscalePre_x4.glsl', f'Anime4K_Restore_CNN_Soft_{sec_qualities[quality]}.glsl',
            f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        ],
        'C+A': [
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Upscale_Denoise_CNN_x2_{quality}.glsl',
            'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl',
            f'Anime4K_Restore_CNN_{sec_qualities[quality]}.glsl',
            f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        ]
    }

    return created_presets[mode]


def to_string(preset=None):
    if preset is None:
        preset = current_preset
    string = ''
    is_first = True
    for shader in preset:
        if not is_first:
            string += ';'
        else:
            is_first = False
        string += os.path.dirname(__file__) + os.sep + 'shaders' + os.sep + shader
    return string
