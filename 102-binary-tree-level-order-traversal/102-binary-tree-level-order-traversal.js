/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if (!root) return [];
    
    const q = [root];
    let res = [];
    
    root.level = 0;
    
    while(q.length) {
        let curr = q.shift();
        
        
        if (!res[curr.level]) {
            res.push([curr.val]);
        }
        else {
            // res[curr.level][res[curr.level].length] = curr.val;
            res[curr.level].push(curr.val) 
        }
        
        
        
        if (curr.left) {
            curr.left.level = curr.level + 1;
            q.push(curr.left);
        }
        if (curr.right) {
            curr.right.level = curr.level + 1;
            q.push(curr.right);
        }
    }
    return res;
};