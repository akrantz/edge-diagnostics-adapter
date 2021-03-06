{
    "variables": {
        "module_name":"Addon",
        "module_path":"../../out/lib/"
    },
    "targets": [
        {
            "target_name": "<(module_name)",
            "sources": [ "EdgeFunctions.cpp", "MessageReceiver.cpp", "stdafx.cpp" ],
            'msvs_precompiled_header': 'stdafx.h',
            'msvs_precompiled_source': 'stdafx.cpp',
            "include_dirs" : [
                "<!(node -e \"require('nan')\")",
                "../Common/",
                "../../out/native/$(ConfigurationName)/$(PlatformName)"
            ],
            "defines": [
                "UNICODE"
            ],
            "libraries": [
                "version.lib",
                "Psapi.lib",
                "../../../out/native/$(ConfigurationName)/$(PlatformName)/Common.lib"
            ],
            'configurations': {
                'Release': {
                    'msvs_settings': {
                        "VCCLCompilerTool": {
                            'WholeProgramOptimization': 'false',
                        }
                    },
                }
            }
        },
        {
            "target_name": "action_after_build",
            "type": "none",
            "dependencies": [ "<(module_name)" ],
            "copies": [
                {
                    "files": [ "<(PRODUCT_DIR)\<(module_name).node" ],
                    "destination": "<(module_path)"
                }
            ]
        }
    ],
}
