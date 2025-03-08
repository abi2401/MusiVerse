from openai import OpenAI
import os
import json

def generate_lyric(prompt):
    '''try:

        client = OpenAI(api_key="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")

        # Modify prompt to ensure structured output
        formatted_prompt = (
            f"{prompt}\n\n"
            "Generate song lyrics in JSON format with multiple verses, choruses, and optionally a bridge if appropriate.\n"
            "Use this structure:\n"
            "{\n"
            '  "title": "Song Title",\n'
            '  "sections": [\n'
            '    { "section_name": "Verse 1", "lines": ["Line 1", "Line 2", "..."] },\n'
            '    { "section_name": "Chorus", "lines": ["Chorus line 1", "Chorus line 2", "..."] },\n'
            '    { "section_name": "Verse 2", "lines": ["Line 1", "Line 2", "..."] },\n'
            '    { "section_name": "Chorus", "lines": ["Same or modified chorus lines"] },\n'
            '    { "section_name": "Bridge (Optional)", "lines": ["Bridge line 1", "Bridge line 2", "..."] }\n'
            "  ]\n"
            "}"
        )


        # Send request
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": formatted_prompt}]
        )

        # Extract response
        generated_text = response.choices[0].message.content

        # Parse JSON safely
        try:
            response_data = json.loads(generated_text)
        except json.JSONDecodeError:
            return "Error: Failed to parse JSON. Model may have returned unexpected text."

        # Extract title and sections
        title = response_data.get("title", "Untitled Song")
        sections = response_data.get("sections", [])

        # Format lyrics in a structured way
        lyrics_output = f"\n🎵 {title.upper()} 🎵\n"

        for section in sections:
            section_name = section.get("section_name", "").upper()
            lines = section.get("lines", [])

            if "chorus" in section_name.lower():
                lyrics_output += f"\n[CHORUS]\n" + "\n".join(lines) + "\n"
            else:
                lyrics_output += f"\n{section_name}\n" + "\n".join(lines) + "\n"

        return lyrics_output.strip()

    except Exception as e:
        return f"Error: {str(e)}"'''

