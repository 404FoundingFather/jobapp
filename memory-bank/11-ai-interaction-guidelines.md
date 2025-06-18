# AI Interaction Guidelines

## Memory Bank System Overview

### Purpose
This Memory Bank serves as the persistent memory for AI-assisted development, ensuring continuity across sessions despite memory resets. Each file contains essential project knowledge that enables any AI to quickly understand the project and continue development effectively.

### Core Principle
**Critical:** An AI agent MUST read ALL memory bank files at the start of EVERY task. This is not optional - it's the foundation of effective AI-assisted development.

## Memory Bank Structure

### Reading Order for New Sessions
1. **Orientation Phase** (Read First)
   - `00-index.md` - Understanding the documentation structure
   - `01-productVision.md` - Project goals and purpose
   - `03-systemArchitecture.md` - High-level system design and component architecture
   - `04-systemPatterns.md` - Implementation patterns and code organization

2. **Status Assessment Phase** (Read Second)
   - `08-kanban.md` - Current project status and active tasks
   - `09-changelog.md` - Recent changes and project history
   - `07-developmentPlan.md` - Implementation roadmap

3. **Technical Context Phase** (Read as Needed)
   - `02-techContext.md` - Technology stack and setup
   - `05-database.md` - Data models and schema
   - `06-uidesign.md` - UI/UX specifications
   - `10-environment.md` - Development environment details

4. **Reference Phase** (Use During Development)
   - `12-code-snippets.md` - Reusable patterns
   - `13-decisions.md` - Architectural decisions
   - `14-quick-reference.md` - Glossary and commands

5. **Meta Information**
   - `11-ai-interaction-guidelines.md` - This file

## AI Workflow Guidelines

### Session Initialization
1. **Always start by reading the Memory Bank files in order**
2. **Summarize your understanding** of the project state
3. **Identify the current focus area** from the Kanban board
4. **Check for any blockers or dependencies** before proceeding
5. **Confirm the development approach** with the established patterns

### Task Execution
1. **Reference established patterns** from the Memory Bank
2. **Follow the coding standards** defined in system patterns
3. **Use the component library** and design system specifications
4. **Implement features according to** the development plan
5. **Update relevant Memory Bank files** after significant changes

### Code Development Standards

#### File Organization
Follow the structure defined in `04-systemPatterns.md`:
- Use established naming conventions
- Follow the defined folder structure
- Implement consistent coding patterns
- Maintain the established architecture

#### Quality Standards
- **Code Reviews:** Follow the review process outlined
- **Testing:** Implement tests according to the testing strategy
- **Documentation:** Update documentation for new features
- **Performance:** Meet performance benchmarks defined

### Communication Patterns

#### Progress Updates
- Update `08-kanban.md` when task status changes
- Add entries to `09-changelog.md` for completed features
- Document decisions in `13-decisions.md` when making architectural choices

#### Problem Resolution
- Check `14-quick-reference.md` for common solutions
- Reference `12-code-snippets.md` for implementation patterns
- Review `13-decisions.md` for context on previous choices

## Memory Bank Maintenance

### When to Update Files

#### Immediate Updates Required
- **System Patterns** - When changing architecture or coding standards
- **Database Schema** - When modifying data models or relationships
- **UI Design** - When updating design system or components
- **Technical Context** - When adding/changing technologies

#### Regular Updates Required
- **Kanban Board** - Daily during active development
- **Development Plan** - Weekly or when priorities change
- **Changelog** - After each feature completion or release

#### Milestone Updates
- **Product Vision** - When project scope or goals evolve
- **Environment** - When deployment or infrastructure changes
- **Quick Reference** - When adding new commands or concepts

### Quality Guidelines for Updates
1. **Be Specific:** Provide concrete details, not vague descriptions
2. **Include Context:** Explain why decisions were made
3. **Update Related Files:** Ensure consistency across files
4. **Maintain Format:** Follow established templates and structures
5. **Include Examples:** Provide code examples and usage patterns

## Project Context Management

### Understanding Project State
Before making any changes, ensure you understand:
- **Current Sprint Goals** - From the Kanban board
- **Recent Changes** - From the changelog
- **Technical Debt** - From the development plan
- **Architectural Constraints** - From system patterns
- **User Requirements** - From the product vision

### Making Informed Decisions
- **Check Previous Decisions** - Review architectural decision records
- **Consider Impact** - Think about effects on other system components
- **Maintain Consistency** - Follow established patterns and conventions
- **Document Rationale** - Explain why you chose specific approaches

## Development Best Practices

### Code Implementation
```typescript
// Follow established patterns from system-patterns.md
// Use naming conventions defined in the Memory Bank
// Implement features according to the development plan
// Follow the UI design specifications

// Example: Component implementation following project patterns
interface [ComponentName]Props {
  // Props according to established patterns
}

export const [ComponentName]: React.FC<[ComponentName]Props> = ({
  // Implementation following project standards
}) => {
  // Component logic following established patterns
  return (
    // JSX following UI design specifications
  );
};
```

### Database Changes
```sql
-- Follow schema patterns from database.md
-- Use established naming conventions
-- Include proper indexes and constraints
-- Document changes in changelog

-- Example: Following established database patterns
CREATE TABLE [table_name] (
  -- Structure following project conventions
);
```

### Testing Implementation
```typescript
// Follow testing patterns from system-patterns.md
// Use established test structure and naming
// Ensure adequate coverage as defined in development plan

describe('[Component/Function Name]', () => {
  // Test implementation following project standards
});
```

## Error Handling & Recovery

### When Things Go Wrong
1. **Check Memory Bank Files** - Often solutions are already documented
2. **Review Recent Changes** - Check changelog for related modifications
3. **Consult Quick Reference** - Look for troubleshooting guides
4. **Document the Issue** - Add to changelog or decisions file
5. **Update Memory Bank** - Prevent similar issues in the future

### Learning from Issues
- **Document Solutions** - Add to quick reference for future use
- **Update Patterns** - Improve system patterns based on learnings
- **Enhance Guidelines** - Update this file with new insights

## Collaboration Guidelines

### Working with Human Developers
- **Respect Established Patterns** - Don't introduce inconsistent approaches
- **Communicate Changes** - Update Memory Bank files when making modifications
- **Ask for Clarification** - When project requirements are unclear
- **Provide Context** - Explain AI decision-making process when helpful

### Code Review Process
- **Follow Review Guidelines** - As defined in system patterns
- **Reference Memory Bank** - Show how changes align with project standards
- **Update Documentation** - Ensure Memory Bank reflects implemented changes

## Continuous Improvement

### Memory Bank Evolution
- **Regular Reviews** - Periodically assess Memory Bank effectiveness
- **Template Updates** - Improve file templates based on usage
- **Process Refinement** - Enhance AI workflow based on experience
- **Knowledge Capture** - Document new patterns and practices

### Feedback Integration
- **User Feedback** - Incorporate developer suggestions for improvements
- **Performance Metrics** - Track effectiveness of AI-assisted development
- **Pattern Recognition** - Identify recurring issues and solutions

---

## Quick Reference for AI Agents

### Session Checklist
- [ ] Read all Memory Bank files in order
- [ ] Understand current project status from Kanban
- [ ] Review recent changes from changelog
- [ ] Check for active blockers or dependencies
- [ ] Confirm development approach with established patterns

### Before Making Changes
- [ ] Reference relevant Memory Bank files
- [ ] Follow established coding standards
- [ ] Consider impact on other system components
- [ ] Plan for testing and documentation updates

### After Making Changes
- [ ] Update relevant Memory Bank files
- [ ] Move Kanban items to appropriate status
- [ ] Add changelog entries for significant changes
- [ ] Document any new patterns or decisions

---
*These guidelines ensure effective AI-assisted development while maintaining project consistency and quality.* 