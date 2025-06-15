# Contributing to Enhanced QR Code MCP Server

Thank you for your interest in contributing to the Enhanced QR Code MCP Server! This project builds upon the excellent foundation of [@jwalsh/mcp-server-qrcode](https://github.com/jwalsh/mcp-server-qrcode) and we welcome contributions that enhance its capabilities.

## 🚀 Quick Start

1. **Fork the repository**
   ```bash
   git clone https://github.com/myownipgit/enhanced-qrcode-mcp.git
   cd enhanced-qrcode-mcp
   ```

2. **Set up development environment**
   ```bash
   ./setup.sh
   source venv/bin/activate
   ```

3. **Run tests**
   ```bash
   python3 tests/test_server.py
   ```

## 🛠️ Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use type hints where possible
- Include docstrings for all functions and classes
- Keep functions focused and well-named

### Testing
- All new features must include tests
- Tests should cover both success and error cases
- Run the full test suite before submitting PRs
- Aim for comprehensive test coverage

### Documentation
- Update README.md for new features
- Add usage examples to `examples/usage_examples.md`
- Include docstrings with clear parameter descriptions
- Update the changelog for notable changes

## 🎯 Areas for Contribution

### High Priority
- **New Content Types**: Add support for additional QR code formats
- **Performance Optimization**: Improve batch processing speed
- **Error Handling**: Enhanced error messages and recovery
- **Documentation**: More usage examples and tutorials

### Medium Priority
- **Configuration Options**: More customizable parameters
- **Output Formats**: Support for additional image formats (SVG, etc.)
- **Integration Examples**: Sample integrations with other tools
- **Validation**: Content validation before QR generation

### Advanced Features
- **Database Integration**: Optional database storage for metadata
- **Web Interface**: Simple web UI for non-technical users
- **Custom Templates**: Branded QR code templates
- **Batch Import**: CSV/JSON file import for mass generation

## 📝 Submission Process

### Pull Request Guidelines

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clean, well-documented code
   - Add or update tests
   - Update documentation

3. **Test your changes**
   ```bash
   python3 tests/test_server.py
   # Ensure all tests pass
   ```

4. **Commit with clear messages**
   ```bash
   git commit -m "feat: add support for SVG output format"
   git commit -m "docs: update usage examples with SVG examples"
   git commit -m "test: add SVG generation tests"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

### PR Requirements
- [ ] Clear description of changes
- [ ] Tests pass completely
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
- [ ] Follows project coding standards

## 🐛 Bug Reports

### Before Reporting
- Check existing issues for duplicates
- Verify the bug with the latest version
- Test with minimal reproduction case

### Bug Report Template
```markdown
**Bug Description**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Generate QR code with parameters: ...
2. Run command: ...
3. See error: ...

**Expected Behavior**
What you expected to happen.

**Environment**
- Python version: 
- MCP version: 
- Operating System: 
- QR code content type: 

**Additional Context**
Any other context about the problem.
```

## 💡 Feature Requests

### Feature Request Template
```markdown
**Feature Description**
A clear description of the feature you'd like to see.

**Use Case**
Describe the problem this feature would solve.

**Proposed Solution**
How you envision this feature working.

**Alternatives**
Other approaches you've considered.

**Additional Context**
Any other context or screenshots about the feature.
```

## 🙏 Acknowledgments

This project builds upon the excellent work of:
- [@jwalsh/mcp-server-qrcode](https://github.com/jwalsh/mcp-server-qrcode) - Original foundation
- [Model Context Protocol](https://github.com/modelcontextprotocol) - Protocol specification
- [python-qrcode](https://github.com/lincolnloop/python-qrcode) - Core QR generation
- [Pillow](https://github.com/python-pillow/Pillow) - Image processing

We appreciate all contributors who help make this project better! 🎉