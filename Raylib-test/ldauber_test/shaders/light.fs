#version 330

in vec3 fragPosition;
in vec2 fragTexCoord;
in vec4 fragColor;

uniform vec4 colDiffuse;
out vec4 finalColor;

// Variables dynamiques envoyées par Python
uniform vec3 cameraPos;
uniform float fogRadius;
uniform vec3 lightColor;   // Couleur de la lampe (RGB)
uniform int lightOn;       // 1 = Allumée, 0 = Éteinte

void main()
{
    vec4 baseColor = colDiffuse * fragColor;
    float distance = length(cameraPos - fragPosition);

    // 1. Lumière ambiante de base (0.08 = les objets au loin restent très légèrement visibles)
    float ambient = 0.08;
    float lightFactor = ambient;

    // 2. Si la lampe est allumée, on calcule le halo de lumière progressif
    if (lightOn == 1) {
        float radialFactor = 1.0 - (distance / fogRadius);
        radialFactor = clamp(radialFactor, 0.0, 1.0);
        
        // On combine la lumière ambiante et l'apport de la lampe
        lightFactor = clamp(ambient + radialFactor, 0.0, 1.0);
    }

    // 3. Application de la couleur de la lampe sur le facteur dynamique
    // Si la lampe est éteinte, seul l'ambient (gris neutre) s'applique.
    vec3 finalLight = vec3(ambient);
    if (lightOn == 1) {
        float radialFactor = clamp(1.0 - (distance / fogRadius), 0.0, 1.0);
        finalLight = mix(vec3(ambient), lightColor, radialFactor);
    } else {
        finalLight = vec3(ambient);
    }

    finalColor = vec4(baseColor.rgb * finalLight, baseColor.a);
}