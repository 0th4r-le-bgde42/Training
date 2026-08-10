#version 330

in vec2 fragTexCoord;
in vec4 fragColor;

out vec4 finalColor;

uniform sampler2D texture0;
uniform float time;

float rand(vec2 co) {
    return fract(sin(dot(co, vec2(12.9898, 78.233))) * 43758.5453);
}

void main()
{
    // 1. screen effect
    vec2 uv = fragTexCoord - 0.5;
    // Flat screen vec2 uv = fragTextCoord
    uv *= 1.0 + (uv.x * uv.x + uv.y * uv.y) * 0.15; 
    uv += 0.5;

    // Si on déborde, bordure noire
    if (uv.x < 0.0 || uv.x > 1.0 || uv.y < 0.0 || uv.y > 1.0) {
        finalColor = vec4(0.0, 0.0, 0.0, 1.0);
        return;
    }

    // 2. get colors
    vec4 baseColor = texture(texture0, uv);

    // 3. Scanlines
    //float scanline = sin(uv.y * 300.0) * 0.01;
    float scanline = sin(uv.y * 300.0 + (time * 6.0)) * 0.02;
    baseColor.rgb -= scanline;

    baseColor.rgb += (rand(uv) - 0.5) * 0.05;
    finalColor = baseColor * fragColor;
}