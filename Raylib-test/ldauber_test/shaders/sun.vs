#version 330

in vec3 vertexPosition;
in vec2 vertexTexCoord;
in vec3 vertexNormal;      // Reçoit l'orientation de la face du cube
in vec4 vertexColor;

uniform mat4 mvp;
uniform mat4 matModel;

out vec3 fragNormal;       // Transmis au Fragment Shader
out vec4 fragColor;

void main()
{
    // Calcule l'orientation de la normale dans le monde 3D
    fragNormal = normalize(vec3(matModel * vec4(vertexNormal, 0.0)));
    fragColor = vertexColor;
    
    gl_Position = mvp * vec4(vertexPosition, 1.0);
}