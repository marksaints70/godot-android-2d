# Godot per Android, solo 2D

Modello di esportazione Android di Godot compilato su misura per un gioco 2D: senza 3D, fisica e i
moduli che il gioco non usa, ottimizzato per la dimensione. Serve a fare un APK più leggero.

- `custom.py`: le opzioni di compilazione (cosa si toglie e perché).
- `.github/workflows/android.yml`: la compilazione su GitHub Actions (release, arm64).

Per compilare: scheda Actions > "Modello Android" > Run workflow, oppure `gh workflow run android.yml`.
Il risultato è l'artefatto `modello-android-<versione>` con `android_release.apk`, da indicare in
Godot in Esporta > Android > Custom Template > Release.

Quando si aggiorna Godot va cambiato `GODOT_TAG` nel workflow, con la stessa versione dell'editor.
