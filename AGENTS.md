# Gauss-Bonnet Visualization Project

This project builds a 3Blue1Brown-style video series explaining the Gauss-Bonnet theorem.

## Core Goal
Explain advanced differential geometry with:
- full mathematical rigor
- strong visual intuition
- smooth, elegant animation

## Philosophy
- Animate geometry, not equations
- Show intuition FIRST, then reveal math
- Each scene should communicate ONE idea clearly

## Style
- Dark background
- Minimal text
- Smooth transitions (no abrupt motion)
- Clean color scheme:
  - Tangent (e1): yellow
  - Normal (e2): blue
  - Binormal (e3): green
  - Curvature/torsion: red

## Manim Rules
- Manim CE v0.19
- Use Surface, not ParametricSurface
- Avoid SurfaceMesh
- Prefer ValueTracker + always_redraw
- Keep code readable and modular

## Workflow
- One scene per file
- Never modify unrelated files
- If unclear, ask for clarification
- Always prioritize visual clarity over complexity