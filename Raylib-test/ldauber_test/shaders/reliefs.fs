#version 330

in vec3 fragNormal;
in vec4 fragColor;

uniform vec4 colDiffuse;
out vec4 finalColor;

// Variables envoyées par Python
uniform vec3 lightDir;     // Direction d'où vient la lumière (ex: du ciel incliné)
uniform vec3 lightColor;   // Couleur de la lumière (ex: blanc ou jaune)

void main()
{
    vec4 baseColor = colDiffuse * fragColor;

    // 1. Lumière ambiante minimum (pour éviter que les zones d'ombre soient 100% noires)
    float ambientStrength = 0.25;
    vec3 ambient = ambientStrength * lightColor;

    // 2. Calcul de la réflexion diffuse (Lambert) pour le relief
    // Plus la face est face au soleil, plus NdotL est proche de 1.0
    vec3 normal = normalize(fragNormal);
    vec3 lightDirection = normalize(-lightDir); 
    float NdotL = max(dot(normal, lightDirection), 0.0);
    vec3 diffuse = NdotL * lightColor;

    // 3. Combinaison finale
    vec3 lighting = ambient + diffuse;
    finalColor = vec4(baseColor.rgb * lighting, baseColor.a);
}