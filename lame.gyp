{
	'variables':{
		#'library' : 'static_library',
		'library' : 'shared_library',
	},
	
	'target_defaults': {
		
		'msvs_settings': {
			# This magical incantation is necessary because VC++ will compile
			# object files to same directory... even if they have the same name!
			'VCCLCompilerTool': {
			  'ObjectFile': '$(IntDir)/%(RelativeDir)/',
			  'AdditionalOptions': ['/w']
			},
		},
		'configurations':{
			'Debug':{
				'conditions': [
				  ['target_arch=="x64"', {
					'msvs_configuration_platform': 'x64',
				  }],
				],
				'defines':[
					'DEBUG',
				],
				'msvs_settings': {				
					'VCLinkerTool' : {
						'GenerateDebugInformation' : 'true',
						'conditions':[
							['target_arch=="x64"', {
								'TargetMachine' : 17 # /MACHINE:X64
							}],
						],
						
					}
				}
			},
			'Release':{
				'conditions': [
				  ['target_arch=="x64"', {
					'msvs_configuration_platform': 'x64',
				  }],
				],
				'msvs_settings': {				
					'VCLinkerTool' : {
						'conditions':[
							['target_arch=="x64"', {
								'TargetMachine' : 17 # /MACHINE:X64
							}],
						],
						
					}
				}
			},
		},
		
		'conditions': [
			['OS=="linux" and target_arch=="ia32"',{
				'cflags':[
					'-m32',
				],
				'ldflags':[
					'-m32',
					'-L/usr/lib32',
					'-L/usr/lib32/debug',
				],
			}],
			['OS=="linux" and target_arch=="x64"',{
				'cflags':[
					'-m64'
				],
				'ldflags':[
					'-m64',
				],
			}],
		
			['OS == "win"',{
				'defines':[
					#'__ICL',
					#'inline=__inline',
					#'__asm__=__asm',
				],
				'link_settings': {
					'libraries': [
						#'-lShell32.lib',
					]
				 },
				 
			}],
			
			
			
			
		  ['OS != "win"', {
			'cflags':[
				'-std=gnu99',
			],
			
			'conditions': [
				['library == "shared_library"',{
					'cflags':[
						'-fPIC',
						#'-Wno-maybe-uninitialized',
						# '-fomit-frame-pointer',
						# '-fno-tree-vectorize',
					],
					'ldflags':[
						#'-Wl,-Bsymbolic',
					],
				}],
			  ['OS=="solaris"', {
				'cflags': [ '-pthreads' ],
			  }],
			  ['OS not in "solaris android"', {
				'ldflags':[
					'-pthread',
					#'-lm',
					#'-ldl',
				],
			  }],
			  ['OS=="android"',{
				'defines':[
					'ANDROID'
				],
			  }],
			],
		  }],
		],
	  },
	
	'targets':[
		{
			'target_name': 'libmp3lame',
			'type':'<(library)',
			
			'defines':[
				'HAVE_CONFIG_H',
			],
			'hard_dependency': 1,
			'copies':[
				{
					'destination':'include/lame',
					'files':[
						'lame_src/include/lame.h',
					],
				},
			],
			
			'include_dirs':[
				'include',
				'lame_src/include',
				'lame_src/libmp3lame',
				'lame_src/mpglib',
				'config/<(OS)/<(target_arch)',
			],
			'direct_dependent_settings': {
				'include_dirs': [
					'include',
					'lame_src/include',
					'lame_src/libmp3lame',
					

				],
				'conditions':[
					['OS == "win" and library == "shared_library"',{
						'defines':[
							
						],
					}],
				],
			 },
			'sources':[
				'lame_src/libmp3lame/bitstream.c',
				'lame_src/libmp3lame/bitstream.h',
				'lame_src/libmp3lame/encoder.c',
				'lame_src/libmp3lame/encoder.h',
				'lame_src/libmp3lame/fft.c',
				'lame_src/libmp3lame/fft.h',
				'lame_src/libmp3lame/gain_analysis.c',
				'lame_src/libmp3lame/gain_analysis.h',
				'lame_src/libmp3lame/i386',
				'lame_src/libmp3lame/id3tag.c',
				'lame_src/libmp3lame/id3tag.h',
				'lame_src/libmp3lame/l3side.h',
				'lame_src/libmp3lame/lame-analysis.h',
				'lame_src/libmp3lame/lame.c',
				'lame_src/libmp3lame/lame.rc',
				'lame_src/libmp3lame/lameerror.h',
				'lame_src/libmp3lame/lame_global_flags.h',
				'lame_src/libmp3lame/logoe.ico',
				'lame_src/libmp3lame/machine.h',
				'lame_src/libmp3lame/mpglib_interface.c',
				'lame_src/libmp3lame/newmdct.c',
				'lame_src/libmp3lame/newmdct.h',
				'lame_src/libmp3lame/presets.c',
				'lame_src/libmp3lame/psymodel.c',
				'lame_src/libmp3lame/psymodel.h',
				'lame_src/libmp3lame/quantize.c',
				'lame_src/libmp3lame/quantize.h',
				'lame_src/libmp3lame/quantize_pvt.c',
				'lame_src/libmp3lame/quantize_pvt.h',
				'lame_src/libmp3lame/reservoir.c',
				'lame_src/libmp3lame/reservoir.h',
				'lame_src/libmp3lame/set_get.c',
				'lame_src/libmp3lame/set_get.h',
				'lame_src/libmp3lame/tables.c',
				'lame_src/libmp3lame/tables.h',
				'lame_src/libmp3lame/takehiro.c',
				'lame_src/libmp3lame/util.c',
				'lame_src/libmp3lame/util.h',
				'lame_src/libmp3lame/vbrquantize.c',
				'lame_src/libmp3lame/vbrquantize.h',
				'lame_src/libmp3lame/VbrTag.c',
				'lame_src/libmp3lame/VbrTag.h',
				'lame_src/libmp3lame/version.c',
				'lame_src/libmp3lame/version.h',
				
				'lame_src/mpglib/AUTHORS',
				'lame_src/mpglib/common.c',
				'lame_src/mpglib/common.h',
				'lame_src/mpglib/dct64_i386.c',
				'lame_src/mpglib/dct64_i386.h',
				'lame_src/mpglib/decode_i386.c',
				'lame_src/mpglib/decode_i386.h',
				'lame_src/mpglib/huffman.h',
				'lame_src/mpglib/interface.c',
				'lame_src/mpglib/interface.h',
				'lame_src/mpglib/l2tables.h',
				'lame_src/mpglib/layer1.c',
				'lame_src/mpglib/layer1.h',
				'lame_src/mpglib/layer2.c',
				'lame_src/mpglib/layer2.h',
				'lame_src/mpglib/layer3.c',
				'lame_src/mpglib/layer3.h',
				'lame_src/mpglib/mpg123.h',
				'lame_src/mpglib/mpglib.h',
				'lame_src/mpglib/README',
				'lame_src/mpglib/tabinit.c',
				'lame_src/mpglib/tabinit.h',
			],
			
			'conditions':[
				['target_arch in "ia32 x64"',{
					'sources':[
						'lame_src/libmp3lame/vector/xmm_quantize_sub.c',
					],
				}],
				['OS == "win"',{
					'sources':[
						'lame_src/include/lame.def',
					],
				}],
			],
		},
		
		
		# test program that prints the version number
		{
		  'target_name': 'test',
		  'type': 'executable',
		  'dependencies': [ 'libmp3lame' ],
		  'sources': [ 'test.c' ]
		},
	
	
	],
	
	'conditions':[
		['OS == "win"',{
			'targets':[
				{
					'target_name':'lame_test',
					'type':'executable',
					'dependencies':[
						'libmp3lame',
					],
					'sources':[
						'lame_src/test/lame_test.cpp',
					],
					
				},
				
				{
					'target_name':'mp3rtp',
					'type':'executable',
					'defines':[
						'HAVE_CONFIG_H',
					],
					'include_dirs':[
						'config/<(OS)/<(target_arch)',
					],
					'dependencies':[
						'libmp3lame',
					],
					'sources':[
						'lame_src/frontend/main.c',
						'lame_src/frontend/main.h',
						'lame_src/frontend/mp3rtp.c',
						'lame_src/frontend/rtp.c',
						'lame_src/frontend/rtp.h',
						
						'lame_src/frontend/console.c',
						'lame_src/frontend/console.h',
						
						'lame_src/frontend/get_audio.c',
						'lame_src/frontend/get_audio.h',
						
						'lame_src/frontend/parse.c',
						'lame_src/frontend/parse.h',
						
						'lame_src/frontend/lametime.c',
						'lame_src/frontend/lametime.h',
						
					],
					'conditions':[
						['OS == "win"',{
							'link_settings': {
								'libraries': [
									'-lws2_32.lib'
								]
							}
						}],
						['OS == "linux"',{
							'ldflags' : [
								
							],
						}],
					],
				},
				
				{
					'target_name':'mp3x',
					'type':'executable',
					'defines':[
						'HAVE_CONFIG_H',
					],
					'include_dirs':[
						'config/<(OS)/<(target_arch)',
					],
					'dependencies':[
						'libmp3lame',
					],
					'sources':[
						'lame_src/frontend/amiga_mpega.c',
						'lame_src/frontend/brhist.c',
						'lame_src/frontend/brhist.h',
						'lame_src/frontend/console.c',
						'lame_src/frontend/console.h',

						'lame_src/frontend/get_audio.c',
						'lame_src/frontend/get_audio.h',
						

						'lame_src/frontend/lametime.c',
						'lame_src/frontend/lametime.h',
						'lame_src/frontend/lame_main.c',
						'lame_src/frontend/main.c',
						'lame_src/frontend/main.h',
						
						
						'lame_src/frontend/parse.c',
						'lame_src/frontend/parse.h',
						
						'lame_src/frontend/timestatus.c',
						'lame_src/frontend/timestatus.h',
					
					],
					
					
					'conditions':[
						['OS == "linux"',{
							'sources':[
								#'lame_src/frontend/gpkplotting.c',
								#'lame_src/frontend/gpkplotting.h',
								#'lame_src/frontend/gtkanal.c',
								#'lame_src/frontend/gtkanal.h',
								#'lame_src/frontend/mp3x.c',
							],
							'ldflags' : [
								'-lreadline',
							],
						}],
						['OS == "win"',{
							'link_settings': {
								'libraries': [
									'-lws2_32.lib'
								]
							}
						}]
					],
				}
			],
		}],
	],
	
}