#!/usr/bin/env python3
"""
Test Script for Enhanced QR Code MCP Server
Demonstrates all functionality and validates the implementation
"""

import json
import os
import sys
from pathlib import Path

# Add the src directory to path to import the server
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from enhanced_qrcode_server import (
        create_qr_code_image, 
        generate_filename, 
        save_metadata
    )
    import qrcode
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Run setup.sh first to install dependencies")
    sys.exit(1)

def test_qr_generation():
    """Test basic QR code generation"""
    print("🧪 Testing QR code generation...")
    
    try:
        qr = create_qr_code_image("Test content", "M", 10, 4)
        img = qr.make_image(fill_color="black", back_color="white")
        print("✅ QR code generation successful")
        return True
    except Exception as e:
        print(f"❌ QR code generation failed: {e}")
        return False

def test_filename_generation():
    """Test filename generation logic"""
    print("🧪 Testing filename generation...")
    
    # Test custom filename
    filename1 = generate_filename("test content", "custom_name")
    assert filename1 == "custom_name", f"Expected 'custom_name', got '{filename1}'"
    
    # Test ID-based filename
    filename2 = generate_filename("test content", "", "test_id")
    assert filename2 == "qr_test_id", f"Expected 'qr_test_id', got '{filename2}'"
    
    # Test auto-generated filename
    filename3 = generate_filename("Hello World!")
    assert filename3.startswith("qr_"), f"Auto-generated filename should start with 'qr_'"
    assert "Hello_World" in filename3, f"Auto-generated filename should contain content preview"
    
    print("✅ Filename generation tests passed")
    return True

def test_file_operations():
    """Test file saving and metadata generation"""
    print("🧪 Testing file operations...")
    
    test_dir = "./test_output"
    Path(test_dir).mkdir(parents=True, exist_ok=True)
    
    try:
        # Generate test QR code
        qr = create_qr_code_image("Test file operations", "M", 10, 4)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save PNG file
        test_file = os.path.join(test_dir, "test_qr.png")
        img.save(test_file)
        
        # Check file exists
        assert os.path.exists(test_file), "PNG file was not created"
        
        # Test metadata generation
        parameters = {"error_correction": "M", "size": 5}
        metadata_path = save_metadata(test_file, "Test file operations", parameters)
        
        # Check metadata file exists
        assert os.path.exists(metadata_path), "Metadata file was not created"
        
        # Validate metadata content
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
        
        assert metadata["content"] == "Test file operations", "Metadata content mismatch"
        assert metadata["parameters"]["error_correction"] == "M", "Metadata parameters mismatch"
        
        print("✅ File operations tests passed")
        return True
        
    except Exception as e:
        print(f"❌ File operations test failed: {e}")
        return False

def test_integration_example():
    """Create a complete integration example"""
    print("🧪 Testing complete integration example...")
    
    test_dir = "./integration_test"
    Path(test_dir).mkdir(parents=True, exist_ok=True)
    
    # Test data
    test_qr_codes = [
        {"id": "text_test", "content": "Hello Integration Test!", "type": "text"},
        {"id": "url_test", "content": "https://github.com/myownipgit/enhanced-qrcode-mcp", "type": "url"},
        {"id": "email_test", "content": "mailto:test@example.com", "type": "email"}
    ]
    
    generated_files = []
    
    try:
        for qr_spec in test_qr_codes:
            # Generate QR code
            qr = create_qr_code_image(qr_spec["content"], "M", 10, 4)
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save file
            filename = f"qr_{qr_spec['id']}.png"
            filepath = os.path.join(test_dir, filename)
            img.save(filepath)
            
            # Generate metadata
            parameters = {
                "id": qr_spec["id"],
                "type": qr_spec["type"],
                "error_correction": "M",
                "size": 5
            }
            metadata_path = save_metadata(filepath, qr_spec["content"], parameters)
            
            generated_files.append({
                "id": qr_spec["id"],
                "type": qr_spec["type"],
                "filename": filename,
                "filepath": filepath,
                "metadata": metadata_path,
                "size_bytes": os.path.getsize(filepath)
            })
        
        # Create integration manifest
        manifest = {
            "test_date": "2025-06-16",
            "total_generated": len(generated_files),
            "test_directory": test_dir,
            "files": generated_files,
            "test_status": "passed",
            "repository": "https://github.com/myownipgit/enhanced-qrcode-mcp"
        }
        
        manifest_path = os.path.join(test_dir, "integration_test_manifest.json")
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"✅ Integration test passed - {len(generated_files)} files generated")
        print(f"📁 Test files location: {test_dir}")
        print(f"📋 Manifest: {manifest_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return False

def run_all_tests():
    """Run all test functions"""
    print("🚀 Running Enhanced QR Code MCP Server Tests")
    print("Repository: https://github.com/myownipgit/enhanced-qrcode-mcp")
    print("=" * 50)
    
    tests = [
        test_qr_generation,
        test_filename_generation,
        test_file_operations,
        test_integration_example
    ]
    
    passed = 0
    total = len(tests)
    
    for test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ Test {test_func.__name__} crashed: {e}")
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed! Enhanced MCP server is ready to use.")
        print("🔗 Repository: https://github.com/myownipgit/enhanced-qrcode-mcp")
        return True
    else:
        print("⚠️ Some tests failed. Check the output above for details.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)