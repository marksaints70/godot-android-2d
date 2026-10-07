# Opzioni di compilazione del motore per un gioco 2D (va copiato nella radice dei sorgenti di Godot:
# SCons legge custom.py da solo). Si toglie tutto quello che il gioco non usa per un APK più leggero.
# Il gioco è solo 2D (Node2D, Sprite2D, CPUParticles2D, Control), renderer Mobile (Vulkan, con ripiego
# su OpenGL se il telefono non ha Vulkan), font TTF, immagini PNG e WebP, testi in italiano e inglese.
# Se il gioco comincia a usare qualcosa che qui è spento, va riacceso e il motore ricompilato.

production = "yes"
optimize = "size"  # più piccolo invece che più veloce: il gioco è leggero
lto = "full"

# Nodi e server che un gioco 2D senza fisica non usa.
disable_3d = "yes"  # spegne anche fisica 3D, navigazione 3D e XR
disable_physics_2d = "yes"  # il gioco muove tutto da sé, niente corpi fisici
disable_navigation_2d = "yes"

# Testo: il server semplice basta per italiano e inglese (quello completo serve per arabo, hindi,
# thai... e si porta dietro ICU e HarfBuzz).
module_text_server_adv_enabled = "no"
module_text_server_fb_enabled = "yes"

# Moduli spenti: formati, rete, 3D, strumenti dell'editor. Restano gdscript, freetype, webp, svg
# (icone del tema predefinito), glslang (shader Vulkan), ogg e vorbis (l'audio arriverà).
module_astcenc_enabled = "no"
module_basis_universal_enabled = "no"
module_bcdec_enabled = "no"
module_betsy_enabled = "no"
module_bmp_enabled = "no"
module_camera_enabled = "no"
module_csg_enabled = "no"
module_cvtt_enabled = "no"
module_dds_enabled = "no"
module_enet_enabled = "no"
module_etcpak_enabled = "no"
module_fbx_enabled = "no"
module_gltf_enabled = "no"
module_godot_physics_2d_enabled = "no"
module_godot_physics_3d_enabled = "no"
module_gridmap_enabled = "no"
module_hdr_enabled = "no"
module_interactive_music_enabled = "no"
module_jolt_physics_enabled = "no"
module_jpg_enabled = "no"
module_jsonrpc_enabled = "no"
module_ktx_enabled = "no"
module_lightmapper_rd_enabled = "no"
module_mbedtls_enabled = "no"  # niente rete: da riaccendere per classifiche o salvataggi nel cloud
module_meshoptimizer_enabled = "no"
module_mobile_vr_enabled = "no"
module_mp3_enabled = "no"
module_msdfgen_enabled = "no"  # il font non usa MSDF
module_multiplayer_enabled = "no"
module_navigation_2d_enabled = "no"
module_navigation_3d_enabled = "no"
module_noise_enabled = "no"
module_objectdb_profiler_enabled = "no"
module_openxr_enabled = "no"
module_raycast_enabled = "no"
module_regex_enabled = "no"
module_tga_enabled = "no"
module_theora_enabled = "no"
module_tinyexr_enabled = "no"
module_upnp_enabled = "no"
module_vhacd_enabled = "no"
module_visual_shader_enabled = "no"
module_webrtc_enabled = "no"
module_websocket_enabled = "no"
module_webxr_enabled = "no"
module_xatlas_unwrap_enabled = "no"
module_zip_enabled = "no"
