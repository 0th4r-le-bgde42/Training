#version 330

// Reçu du Vertex Shader personnalisé
in vec3 fragPosition;
in vec2 fragTexCoord;
in vec4 fragColor;

uniform vec4 colDiffuse;
out vec4 finalColor;

uniform vec3 cameraPos;
uniform float fogRadius;

void main()
{
    // Distance réelle entre la caméra et le point du mur/sol
    float distance = length(cameraPos - fragPosition);

    // Atténuation de la lumière
    float factor = 1.0 - (distance / fogRadius);
    factor = clamp(factor, 0.0, 1.0);

    vec4 baseColor = colDiffuse * fragColor;
    finalColor = vec4(baseColor.rgb * factor, baseColor.a);
}