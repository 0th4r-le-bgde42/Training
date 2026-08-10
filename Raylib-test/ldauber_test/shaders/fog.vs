#version 330

// Attributs d'entrée par défaut de Raylib
in vec3 vertexPosition;
in vec2 vertexTexCoord;
in vec4 vertexColor;

// Matrices envoyées automatiquement par Raylib
uniform mat4 mvp;
uniform mat4 matModel;

// Données transmises au Fragment Shader
out vec3 fragPosition;
out vec2 fragTexCoord;
out vec4 fragColor;

void main()
{
    // Calcule la vraie position 3D dans le monde (World Space)
    fragPosition = vec3(matModel * vec4(vertexPosition, 1.0));
    fragTexCoord = vertexTexCoord;
    fragColor = vertexColor;

    // Position finale à l'écran
    gl_Position = mvp * vec4(vertexPosition, 1.0);
}