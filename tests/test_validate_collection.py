import unittest
from copy import deepcopy

from scripts.validate_collection import validate_manifest


VALID = {
    "schema_version": "1.0.0",
    "collection": "Halloween 2026",
    "projects": [{
        "id": "example-project",
        "name": "Example Project",
        "repository": "https://github.com/example/project",
        "purpose": "A local research tool.",
        "human_guide": "https://github.com/example/project/blob/main/docs/HUMAN.md",
        "agent_guide": "https://github.com/example/project/blob/main/docs/AGENT.md"
    }],
    "limitations": ["Index only."]
}


class CollectionManifestTests(unittest.TestCase):
    def test_accepts_valid_manifest(self):
        self.assertEqual(validate_manifest(VALID), [])

    def test_rejects_non_object_and_empty_projects(self):
        self.assertIn("manifest must be a JSON object", validate_manifest([]))
        errors = validate_manifest({"schema_version": "1.0.0", "collection": "X", "projects": [], "limitations": []})
        self.assertTrue(any("non-empty array" in error for error in errors))

    def test_rejects_duplicate_or_invalid_ids(self):
        data = deepcopy(VALID)
        data["projects"].append(deepcopy(data["projects"][0]))
        errors = validate_manifest(data)
        self.assertTrue(any("duplicated" in error for error in errors))

        data["projects"][0]["id"] = "Not A Slug"
        self.assertTrue(any("lowercase slug" in error for error in validate_manifest(data)))

    def test_rejects_invalid_url_ports(self):
        data = deepcopy(VALID)
        data["projects"][0]["repository"] = "https://github.com:invalid/example/project"
        errors = validate_manifest(data)
        self.assertTrue(any("repository must be" in error for error in errors))

    def test_rejects_noncanonical_repository_hosts(self):
        data = deepcopy(VALID)
        data["projects"][0]["repository"] = "https://github.com.evil.example/example/project"
        errors = validate_manifest(data)
        self.assertTrue(any("repository must be" in error for error in errors))

    def test_guides_must_belong_to_same_repository(self):
        data = deepcopy(VALID)
        data["projects"][0]["agent_guide"] = "https://github.com/other/project/blob/main/AGENT.md"
        errors = validate_manifest(data)
        self.assertTrue(any("agent_guide" in error for error in errors))

    def test_rejects_empty_required_fields_and_bad_limitations(self):
        data = deepcopy(VALID)
        data["projects"][0]["purpose"] = " "
        data["limitations"] = ["ok", ""]
        errors = validate_manifest(data)
        self.assertTrue(any(".purpose" in error for error in errors))
        self.assertTrue(any("limitations" in error for error in errors))

    def test_rejects_non_markdown_guides(self):
        data = deepcopy(VALID)
        data["projects"][0]["human_guide"] = "https://github.com/example/project/blob/main/docs/guide.txt"
        errors = validate_manifest(data)
        self.assertTrue(any("human_guide" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
